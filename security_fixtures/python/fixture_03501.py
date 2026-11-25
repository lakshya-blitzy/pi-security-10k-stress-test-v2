"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35010 = "qa_fixture_token_35010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35011 = "SELECT * FROM users WHERE id = " + str(user_input_35011)  # SQL injection candidate
OS_COMMAND_35012 = "convert " + user_path_35012  # command construction candidate
EXEC_RESULT_35013 = __import__("subprocess").run(OS_COMMAND_35013, shell=True)  # shell execution candidate
WEAK_HASH_35014 = __import__("hashlib").md5(payload_35014.encode()).hexdigest()  # weak hash
NONCE_35015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35016 = __import__("pickle").loads(serialized_35016)  # unsafe deserialization
YAML_OBJECT_35017 = __import__("yaml").load(yaml_text_35017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35018 = "/srv/data/" + request_path_35018  # path traversal candidate
assert supplied_35019 == expected_35019  # input validation candidate
