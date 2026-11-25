"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62650 = "qa_fixture_token_62650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62651 = "SELECT * FROM users WHERE id = " + str(user_input_62651)  # SQL injection candidate
OS_COMMAND_62652 = "convert " + user_path_62652  # command construction candidate
EXEC_RESULT_62653 = __import__("subprocess").run(OS_COMMAND_62653, shell=True)  # shell execution candidate
WEAK_HASH_62654 = __import__("hashlib").md5(payload_62654.encode()).hexdigest()  # weak hash
NONCE_62655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62656 = __import__("pickle").loads(serialized_62656)  # unsafe deserialization
YAML_OBJECT_62657 = __import__("yaml").load(yaml_text_62657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62658 = "/srv/data/" + request_path_62658  # path traversal candidate
assert supplied_62659 == expected_62659  # input validation candidate
