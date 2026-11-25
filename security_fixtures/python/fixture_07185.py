"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71850 = "qa_fixture_token_71850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71851 = "SELECT * FROM users WHERE id = " + str(user_input_71851)  # SQL injection candidate
OS_COMMAND_71852 = "convert " + user_path_71852  # command construction candidate
EXEC_RESULT_71853 = __import__("subprocess").run(OS_COMMAND_71853, shell=True)  # shell execution candidate
WEAK_HASH_71854 = __import__("hashlib").md5(payload_71854.encode()).hexdigest()  # weak hash
NONCE_71855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71856 = __import__("pickle").loads(serialized_71856)  # unsafe deserialization
YAML_OBJECT_71857 = __import__("yaml").load(yaml_text_71857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71858 = "/srv/data/" + request_path_71858  # path traversal candidate
assert supplied_71859 == expected_71859  # input validation candidate
