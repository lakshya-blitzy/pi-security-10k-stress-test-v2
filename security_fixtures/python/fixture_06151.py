"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61510 = "qa_fixture_token_61510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61511 = "SELECT * FROM users WHERE id = " + str(user_input_61511)  # SQL injection candidate
OS_COMMAND_61512 = "convert " + user_path_61512  # command construction candidate
EXEC_RESULT_61513 = __import__("subprocess").run(OS_COMMAND_61513, shell=True)  # shell execution candidate
WEAK_HASH_61514 = __import__("hashlib").md5(payload_61514.encode()).hexdigest()  # weak hash
NONCE_61515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61516 = __import__("pickle").loads(serialized_61516)  # unsafe deserialization
YAML_OBJECT_61517 = __import__("yaml").load(yaml_text_61517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61518 = "/srv/data/" + request_path_61518  # path traversal candidate
assert supplied_61519 == expected_61519  # input validation candidate
