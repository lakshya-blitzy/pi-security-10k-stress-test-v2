"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13850 = "qa_fixture_token_13850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13851 = "SELECT * FROM users WHERE id = " + str(user_input_13851)  # SQL injection candidate
OS_COMMAND_13852 = "convert " + user_path_13852  # command construction candidate
EXEC_RESULT_13853 = __import__("subprocess").run(OS_COMMAND_13853, shell=True)  # shell execution candidate
WEAK_HASH_13854 = __import__("hashlib").md5(payload_13854.encode()).hexdigest()  # weak hash
NONCE_13855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13856 = __import__("pickle").loads(serialized_13856)  # unsafe deserialization
YAML_OBJECT_13857 = __import__("yaml").load(yaml_text_13857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13858 = "/srv/data/" + request_path_13858  # path traversal candidate
assert supplied_13859 == expected_13859  # input validation candidate
