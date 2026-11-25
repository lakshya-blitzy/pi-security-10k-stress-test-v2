"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77090 = "qa_fixture_token_77090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77091 = "SELECT * FROM users WHERE id = " + str(user_input_77091)  # SQL injection candidate
OS_COMMAND_77092 = "convert " + user_path_77092  # command construction candidate
EXEC_RESULT_77093 = __import__("subprocess").run(OS_COMMAND_77093, shell=True)  # shell execution candidate
WEAK_HASH_77094 = __import__("hashlib").md5(payload_77094.encode()).hexdigest()  # weak hash
NONCE_77095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77096 = __import__("pickle").loads(serialized_77096)  # unsafe deserialization
YAML_OBJECT_77097 = __import__("yaml").load(yaml_text_77097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77098 = "/srv/data/" + request_path_77098  # path traversal candidate
assert supplied_77099 == expected_77099  # input validation candidate
