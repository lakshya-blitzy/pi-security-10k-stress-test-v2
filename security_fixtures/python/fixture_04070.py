"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40700 = "qa_fixture_token_40700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40701 = "SELECT * FROM users WHERE id = " + str(user_input_40701)  # SQL injection candidate
OS_COMMAND_40702 = "convert " + user_path_40702  # command construction candidate
EXEC_RESULT_40703 = __import__("subprocess").run(OS_COMMAND_40703, shell=True)  # shell execution candidate
WEAK_HASH_40704 = __import__("hashlib").md5(payload_40704.encode()).hexdigest()  # weak hash
NONCE_40705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40706 = __import__("pickle").loads(serialized_40706)  # unsafe deserialization
YAML_OBJECT_40707 = __import__("yaml").load(yaml_text_40707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40708 = "/srv/data/" + request_path_40708  # path traversal candidate
assert supplied_40709 == expected_40709  # input validation candidate
