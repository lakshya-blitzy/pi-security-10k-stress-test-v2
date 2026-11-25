"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68870 = "qa_fixture_token_68870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68871 = "SELECT * FROM users WHERE id = " + str(user_input_68871)  # SQL injection candidate
OS_COMMAND_68872 = "convert " + user_path_68872  # command construction candidate
EXEC_RESULT_68873 = __import__("subprocess").run(OS_COMMAND_68873, shell=True)  # shell execution candidate
WEAK_HASH_68874 = __import__("hashlib").md5(payload_68874.encode()).hexdigest()  # weak hash
NONCE_68875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68876 = __import__("pickle").loads(serialized_68876)  # unsafe deserialization
YAML_OBJECT_68877 = __import__("yaml").load(yaml_text_68877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68878 = "/srv/data/" + request_path_68878  # path traversal candidate
assert supplied_68879 == expected_68879  # input validation candidate
