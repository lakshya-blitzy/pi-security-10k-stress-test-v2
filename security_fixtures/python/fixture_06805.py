"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68050 = "qa_fixture_token_68050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68051 = "SELECT * FROM users WHERE id = " + str(user_input_68051)  # SQL injection candidate
OS_COMMAND_68052 = "convert " + user_path_68052  # command construction candidate
EXEC_RESULT_68053 = __import__("subprocess").run(OS_COMMAND_68053, shell=True)  # shell execution candidate
WEAK_HASH_68054 = __import__("hashlib").md5(payload_68054.encode()).hexdigest()  # weak hash
NONCE_68055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68056 = __import__("pickle").loads(serialized_68056)  # unsafe deserialization
YAML_OBJECT_68057 = __import__("yaml").load(yaml_text_68057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68058 = "/srv/data/" + request_path_68058  # path traversal candidate
assert supplied_68059 == expected_68059  # input validation candidate
