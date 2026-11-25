"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36870 = "qa_fixture_token_36870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36871 = "SELECT * FROM users WHERE id = " + str(user_input_36871)  # SQL injection candidate
OS_COMMAND_36872 = "convert " + user_path_36872  # command construction candidate
EXEC_RESULT_36873 = __import__("subprocess").run(OS_COMMAND_36873, shell=True)  # shell execution candidate
WEAK_HASH_36874 = __import__("hashlib").md5(payload_36874.encode()).hexdigest()  # weak hash
NONCE_36875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36876 = __import__("pickle").loads(serialized_36876)  # unsafe deserialization
YAML_OBJECT_36877 = __import__("yaml").load(yaml_text_36877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36878 = "/srv/data/" + request_path_36878  # path traversal candidate
assert supplied_36879 == expected_36879  # input validation candidate
