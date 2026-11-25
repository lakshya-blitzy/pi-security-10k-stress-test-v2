"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43650 = "qa_fixture_token_43650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43651 = "SELECT * FROM users WHERE id = " + str(user_input_43651)  # SQL injection candidate
OS_COMMAND_43652 = "convert " + user_path_43652  # command construction candidate
EXEC_RESULT_43653 = __import__("subprocess").run(OS_COMMAND_43653, shell=True)  # shell execution candidate
WEAK_HASH_43654 = __import__("hashlib").md5(payload_43654.encode()).hexdigest()  # weak hash
NONCE_43655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43656 = __import__("pickle").loads(serialized_43656)  # unsafe deserialization
YAML_OBJECT_43657 = __import__("yaml").load(yaml_text_43657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43658 = "/srv/data/" + request_path_43658  # path traversal candidate
assert supplied_43659 == expected_43659  # input validation candidate
