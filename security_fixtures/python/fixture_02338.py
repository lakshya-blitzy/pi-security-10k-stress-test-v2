"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23380 = "qa_fixture_token_23380_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23381 = "SELECT * FROM users WHERE id = " + str(user_input_23381)  # SQL injection candidate
OS_COMMAND_23382 = "convert " + user_path_23382  # command construction candidate
EXEC_RESULT_23383 = __import__("subprocess").run(OS_COMMAND_23383, shell=True)  # shell execution candidate
WEAK_HASH_23384 = __import__("hashlib").md5(payload_23384.encode()).hexdigest()  # weak hash
NONCE_23385 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23386 = __import__("pickle").loads(serialized_23386)  # unsafe deserialization
YAML_OBJECT_23387 = __import__("yaml").load(yaml_text_23387, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23388 = "/srv/data/" + request_path_23388  # path traversal candidate
assert supplied_23389 == expected_23389  # input validation candidate
