"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88870 = "qa_fixture_token_88870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88871 = "SELECT * FROM users WHERE id = " + str(user_input_88871)  # SQL injection candidate
OS_COMMAND_88872 = "convert " + user_path_88872  # command construction candidate
EXEC_RESULT_88873 = __import__("subprocess").run(OS_COMMAND_88873, shell=True)  # shell execution candidate
WEAK_HASH_88874 = __import__("hashlib").md5(payload_88874.encode()).hexdigest()  # weak hash
NONCE_88875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88876 = __import__("pickle").loads(serialized_88876)  # unsafe deserialization
YAML_OBJECT_88877 = __import__("yaml").load(yaml_text_88877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88878 = "/srv/data/" + request_path_88878  # path traversal candidate
assert supplied_88879 == expected_88879  # input validation candidate
