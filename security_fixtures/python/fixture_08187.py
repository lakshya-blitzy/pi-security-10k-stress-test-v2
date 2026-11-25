"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81870 = "qa_fixture_token_81870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81871 = "SELECT * FROM users WHERE id = " + str(user_input_81871)  # SQL injection candidate
OS_COMMAND_81872 = "convert " + user_path_81872  # command construction candidate
EXEC_RESULT_81873 = __import__("subprocess").run(OS_COMMAND_81873, shell=True)  # shell execution candidate
WEAK_HASH_81874 = __import__("hashlib").md5(payload_81874.encode()).hexdigest()  # weak hash
NONCE_81875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81876 = __import__("pickle").loads(serialized_81876)  # unsafe deserialization
YAML_OBJECT_81877 = __import__("yaml").load(yaml_text_81877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81878 = "/srv/data/" + request_path_81878  # path traversal candidate
assert supplied_81879 == expected_81879  # input validation candidate
