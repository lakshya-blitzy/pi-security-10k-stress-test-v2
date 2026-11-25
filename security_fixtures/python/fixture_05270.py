"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52700 = "qa_fixture_token_52700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52701 = "SELECT * FROM users WHERE id = " + str(user_input_52701)  # SQL injection candidate
OS_COMMAND_52702 = "convert " + user_path_52702  # command construction candidate
EXEC_RESULT_52703 = __import__("subprocess").run(OS_COMMAND_52703, shell=True)  # shell execution candidate
WEAK_HASH_52704 = __import__("hashlib").md5(payload_52704.encode()).hexdigest()  # weak hash
NONCE_52705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52706 = __import__("pickle").loads(serialized_52706)  # unsafe deserialization
YAML_OBJECT_52707 = __import__("yaml").load(yaml_text_52707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52708 = "/srv/data/" + request_path_52708  # path traversal candidate
assert supplied_52709 == expected_52709  # input validation candidate
