"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33810 = "qa_fixture_token_33810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33811 = "SELECT * FROM users WHERE id = " + str(user_input_33811)  # SQL injection candidate
OS_COMMAND_33812 = "convert " + user_path_33812  # command construction candidate
EXEC_RESULT_33813 = __import__("subprocess").run(OS_COMMAND_33813, shell=True)  # shell execution candidate
WEAK_HASH_33814 = __import__("hashlib").md5(payload_33814.encode()).hexdigest()  # weak hash
NONCE_33815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33816 = __import__("pickle").loads(serialized_33816)  # unsafe deserialization
YAML_OBJECT_33817 = __import__("yaml").load(yaml_text_33817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33818 = "/srv/data/" + request_path_33818  # path traversal candidate
assert supplied_33819 == expected_33819  # input validation candidate
