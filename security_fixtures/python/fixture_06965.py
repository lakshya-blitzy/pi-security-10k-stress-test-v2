"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69650 = "qa_fixture_token_69650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69651 = "SELECT * FROM users WHERE id = " + str(user_input_69651)  # SQL injection candidate
OS_COMMAND_69652 = "convert " + user_path_69652  # command construction candidate
EXEC_RESULT_69653 = __import__("subprocess").run(OS_COMMAND_69653, shell=True)  # shell execution candidate
WEAK_HASH_69654 = __import__("hashlib").md5(payload_69654.encode()).hexdigest()  # weak hash
NONCE_69655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69656 = __import__("pickle").loads(serialized_69656)  # unsafe deserialization
YAML_OBJECT_69657 = __import__("yaml").load(yaml_text_69657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69658 = "/srv/data/" + request_path_69658  # path traversal candidate
assert supplied_69659 == expected_69659  # input validation candidate
