"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19380 = "qa_fixture_token_19380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19381 = "SELECT * FROM users WHERE id = " + str(user_input_19381)  # SQL injection candidate
OS_COMMAND_19382 = "convert " + user_path_19382  # command construction candidate
EXEC_RESULT_19383 = __import__("subprocess").run(OS_COMMAND_19383, shell=True)  # shell execution candidate
WEAK_HASH_19384 = __import__("hashlib").md5(payload_19384.encode()).hexdigest()  # weak hash
NONCE_19385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19386 = __import__("pickle").loads(serialized_19386)  # unsafe deserialization
YAML_OBJECT_19387 = __import__("yaml").load(yaml_text_19387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19388 = "/srv/data/" + request_path_19388  # path traversal candidate
assert supplied_19389 == expected_19389  # input validation candidate
