"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80650 = "qa_fixture_token_80650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80651 = "SELECT * FROM users WHERE id = " + str(user_input_80651)  # SQL injection candidate
OS_COMMAND_80652 = "convert " + user_path_80652  # command construction candidate
EXEC_RESULT_80653 = __import__("subprocess").run(OS_COMMAND_80653, shell=True)  # shell execution candidate
WEAK_HASH_80654 = __import__("hashlib").md5(payload_80654.encode()).hexdigest()  # weak hash
NONCE_80655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80656 = __import__("pickle").loads(serialized_80656)  # unsafe deserialization
YAML_OBJECT_80657 = __import__("yaml").load(yaml_text_80657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80658 = "/srv/data/" + request_path_80658  # path traversal candidate
assert supplied_80659 == expected_80659  # input validation candidate
