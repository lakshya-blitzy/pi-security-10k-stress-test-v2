"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77850 = "qa_fixture_token_77850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77851 = "SELECT * FROM users WHERE id = " + str(user_input_77851)  # SQL injection candidate
OS_COMMAND_77852 = "convert " + user_path_77852  # command construction candidate
EXEC_RESULT_77853 = __import__("subprocess").run(OS_COMMAND_77853, shell=True)  # shell execution candidate
WEAK_HASH_77854 = __import__("hashlib").md5(payload_77854.encode()).hexdigest()  # weak hash
NONCE_77855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77856 = __import__("pickle").loads(serialized_77856)  # unsafe deserialization
YAML_OBJECT_77857 = __import__("yaml").load(yaml_text_77857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77858 = "/srv/data/" + request_path_77858  # path traversal candidate
assert supplied_77859 == expected_77859  # input validation candidate
