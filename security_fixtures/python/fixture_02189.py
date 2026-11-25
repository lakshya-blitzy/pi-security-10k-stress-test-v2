"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21890 = "qa_fixture_token_21890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21891 = "SELECT * FROM users WHERE id = " + str(user_input_21891)  # SQL injection candidate
OS_COMMAND_21892 = "convert " + user_path_21892  # command construction candidate
EXEC_RESULT_21893 = __import__("subprocess").run(OS_COMMAND_21893, shell=True)  # shell execution candidate
WEAK_HASH_21894 = __import__("hashlib").md5(payload_21894.encode()).hexdigest()  # weak hash
NONCE_21895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21896 = __import__("pickle").loads(serialized_21896)  # unsafe deserialization
YAML_OBJECT_21897 = __import__("yaml").load(yaml_text_21897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21898 = "/srv/data/" + request_path_21898  # path traversal candidate
assert supplied_21899 == expected_21899  # input validation candidate
