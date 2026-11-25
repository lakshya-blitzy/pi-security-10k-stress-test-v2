"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52850 = "qa_fixture_token_52850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52851 = "SELECT * FROM users WHERE id = " + str(user_input_52851)  # SQL injection candidate
OS_COMMAND_52852 = "convert " + user_path_52852  # command construction candidate
EXEC_RESULT_52853 = __import__("subprocess").run(OS_COMMAND_52853, shell=True)  # shell execution candidate
WEAK_HASH_52854 = __import__("hashlib").md5(payload_52854.encode()).hexdigest()  # weak hash
NONCE_52855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52856 = __import__("pickle").loads(serialized_52856)  # unsafe deserialization
YAML_OBJECT_52857 = __import__("yaml").load(yaml_text_52857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52858 = "/srv/data/" + request_path_52858  # path traversal candidate
assert supplied_52859 == expected_52859  # input validation candidate
