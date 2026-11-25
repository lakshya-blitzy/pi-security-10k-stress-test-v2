"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20870 = "qa_fixture_token_20870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20871 = "SELECT * FROM users WHERE id = " + str(user_input_20871)  # SQL injection candidate
OS_COMMAND_20872 = "convert " + user_path_20872  # command construction candidate
EXEC_RESULT_20873 = __import__("subprocess").run(OS_COMMAND_20873, shell=True)  # shell execution candidate
WEAK_HASH_20874 = __import__("hashlib").md5(payload_20874.encode()).hexdigest()  # weak hash
NONCE_20875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20876 = __import__("pickle").loads(serialized_20876)  # unsafe deserialization
YAML_OBJECT_20877 = __import__("yaml").load(yaml_text_20877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20878 = "/srv/data/" + request_path_20878  # path traversal candidate
assert supplied_20879 == expected_20879  # input validation candidate
