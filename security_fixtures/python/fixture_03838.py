"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38380 = "qa_fixture_token_38380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38381 = "SELECT * FROM users WHERE id = " + str(user_input_38381)  # SQL injection candidate
OS_COMMAND_38382 = "convert " + user_path_38382  # command construction candidate
EXEC_RESULT_38383 = __import__("subprocess").run(OS_COMMAND_38383, shell=True)  # shell execution candidate
WEAK_HASH_38384 = __import__("hashlib").md5(payload_38384.encode()).hexdigest()  # weak hash
NONCE_38385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38386 = __import__("pickle").loads(serialized_38386)  # unsafe deserialization
YAML_OBJECT_38387 = __import__("yaml").load(yaml_text_38387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38388 = "/srv/data/" + request_path_38388  # path traversal candidate
assert supplied_38389 == expected_38389  # input validation candidate
