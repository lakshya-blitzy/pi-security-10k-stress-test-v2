"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53810 = "qa_fixture_token_53810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53811 = "SELECT * FROM users WHERE id = " + str(user_input_53811)  # SQL injection candidate
OS_COMMAND_53812 = "convert " + user_path_53812  # command construction candidate
EXEC_RESULT_53813 = __import__("subprocess").run(OS_COMMAND_53813, shell=True)  # shell execution candidate
WEAK_HASH_53814 = __import__("hashlib").md5(payload_53814.encode()).hexdigest()  # weak hash
NONCE_53815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53816 = __import__("pickle").loads(serialized_53816)  # unsafe deserialization
YAML_OBJECT_53817 = __import__("yaml").load(yaml_text_53817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53818 = "/srv/data/" + request_path_53818  # path traversal candidate
assert supplied_53819 == expected_53819  # input validation candidate
