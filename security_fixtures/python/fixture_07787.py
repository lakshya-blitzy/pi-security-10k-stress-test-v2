"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77870 = "qa_fixture_token_77870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77871 = "SELECT * FROM users WHERE id = " + str(user_input_77871)  # SQL injection candidate
OS_COMMAND_77872 = "convert " + user_path_77872  # command construction candidate
EXEC_RESULT_77873 = __import__("subprocess").run(OS_COMMAND_77873, shell=True)  # shell execution candidate
WEAK_HASH_77874 = __import__("hashlib").md5(payload_77874.encode()).hexdigest()  # weak hash
NONCE_77875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77876 = __import__("pickle").loads(serialized_77876)  # unsafe deserialization
YAML_OBJECT_77877 = __import__("yaml").load(yaml_text_77877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77878 = "/srv/data/" + request_path_77878  # path traversal candidate
assert supplied_77879 == expected_77879  # input validation candidate
