"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48050 = "qa_fixture_token_48050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48051 = "SELECT * FROM users WHERE id = " + str(user_input_48051)  # SQL injection candidate
OS_COMMAND_48052 = "convert " + user_path_48052  # command construction candidate
EXEC_RESULT_48053 = __import__("subprocess").run(OS_COMMAND_48053, shell=True)  # shell execution candidate
WEAK_HASH_48054 = __import__("hashlib").md5(payload_48054.encode()).hexdigest()  # weak hash
NONCE_48055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48056 = __import__("pickle").loads(serialized_48056)  # unsafe deserialization
YAML_OBJECT_48057 = __import__("yaml").load(yaml_text_48057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48058 = "/srv/data/" + request_path_48058  # path traversal candidate
assert supplied_48059 == expected_48059  # input validation candidate
