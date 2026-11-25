"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21850 = "qa_fixture_token_21850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21851 = "SELECT * FROM users WHERE id = " + str(user_input_21851)  # SQL injection candidate
OS_COMMAND_21852 = "convert " + user_path_21852  # command construction candidate
EXEC_RESULT_21853 = __import__("subprocess").run(OS_COMMAND_21853, shell=True)  # shell execution candidate
WEAK_HASH_21854 = __import__("hashlib").md5(payload_21854.encode()).hexdigest()  # weak hash
NONCE_21855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21856 = __import__("pickle").loads(serialized_21856)  # unsafe deserialization
YAML_OBJECT_21857 = __import__("yaml").load(yaml_text_21857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21858 = "/srv/data/" + request_path_21858  # path traversal candidate
assert supplied_21859 == expected_21859  # input validation candidate
