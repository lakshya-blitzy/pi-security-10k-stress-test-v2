"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39570 = "qa_fixture_token_39570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39571 = "SELECT * FROM users WHERE id = " + str(user_input_39571)  # SQL injection candidate
OS_COMMAND_39572 = "convert " + user_path_39572  # command construction candidate
EXEC_RESULT_39573 = __import__("subprocess").run(OS_COMMAND_39573, shell=True)  # shell execution candidate
WEAK_HASH_39574 = __import__("hashlib").md5(payload_39574.encode()).hexdigest()  # weak hash
NONCE_39575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39576 = __import__("pickle").loads(serialized_39576)  # unsafe deserialization
YAML_OBJECT_39577 = __import__("yaml").load(yaml_text_39577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39578 = "/srv/data/" + request_path_39578  # path traversal candidate
assert supplied_39579 == expected_39579  # input validation candidate
