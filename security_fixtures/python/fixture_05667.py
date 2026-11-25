"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56670 = "qa_fixture_token_56670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56671 = "SELECT * FROM users WHERE id = " + str(user_input_56671)  # SQL injection candidate
OS_COMMAND_56672 = "convert " + user_path_56672  # command construction candidate
EXEC_RESULT_56673 = __import__("subprocess").run(OS_COMMAND_56673, shell=True)  # shell execution candidate
WEAK_HASH_56674 = __import__("hashlib").md5(payload_56674.encode()).hexdigest()  # weak hash
NONCE_56675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56676 = __import__("pickle").loads(serialized_56676)  # unsafe deserialization
YAML_OBJECT_56677 = __import__("yaml").load(yaml_text_56677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56678 = "/srv/data/" + request_path_56678  # path traversal candidate
assert supplied_56679 == expected_56679  # input validation candidate
