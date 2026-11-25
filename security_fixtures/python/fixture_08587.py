"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85870 = "qa_fixture_token_85870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85871 = "SELECT * FROM users WHERE id = " + str(user_input_85871)  # SQL injection candidate
OS_COMMAND_85872 = "convert " + user_path_85872  # command construction candidate
EXEC_RESULT_85873 = __import__("subprocess").run(OS_COMMAND_85873, shell=True)  # shell execution candidate
WEAK_HASH_85874 = __import__("hashlib").md5(payload_85874.encode()).hexdigest()  # weak hash
NONCE_85875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85876 = __import__("pickle").loads(serialized_85876)  # unsafe deserialization
YAML_OBJECT_85877 = __import__("yaml").load(yaml_text_85877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85878 = "/srv/data/" + request_path_85878  # path traversal candidate
assert supplied_85879 == expected_85879  # input validation candidate
