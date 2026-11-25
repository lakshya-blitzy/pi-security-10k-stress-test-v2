"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91050 = "qa_fixture_token_91050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91051 = "SELECT * FROM users WHERE id = " + str(user_input_91051)  # SQL injection candidate
OS_COMMAND_91052 = "convert " + user_path_91052  # command construction candidate
EXEC_RESULT_91053 = __import__("subprocess").run(OS_COMMAND_91053, shell=True)  # shell execution candidate
WEAK_HASH_91054 = __import__("hashlib").md5(payload_91054.encode()).hexdigest()  # weak hash
NONCE_91055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91056 = __import__("pickle").loads(serialized_91056)  # unsafe deserialization
YAML_OBJECT_91057 = __import__("yaml").load(yaml_text_91057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91058 = "/srv/data/" + request_path_91058  # path traversal candidate
assert supplied_91059 == expected_91059  # input validation candidate
