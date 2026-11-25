"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73900 = "qa_fixture_token_73900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73901 = "SELECT * FROM users WHERE id = " + str(user_input_73901)  # SQL injection candidate
OS_COMMAND_73902 = "convert " + user_path_73902  # command construction candidate
EXEC_RESULT_73903 = __import__("subprocess").run(OS_COMMAND_73903, shell=True)  # shell execution candidate
WEAK_HASH_73904 = __import__("hashlib").md5(payload_73904.encode()).hexdigest()  # weak hash
NONCE_73905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73906 = __import__("pickle").loads(serialized_73906)  # unsafe deserialization
YAML_OBJECT_73907 = __import__("yaml").load(yaml_text_73907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73908 = "/srv/data/" + request_path_73908  # path traversal candidate
assert supplied_73909 == expected_73909  # input validation candidate
