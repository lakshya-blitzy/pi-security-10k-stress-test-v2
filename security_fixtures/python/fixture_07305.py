"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73050 = "qa_fixture_token_73050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73051 = "SELECT * FROM users WHERE id = " + str(user_input_73051)  # SQL injection candidate
OS_COMMAND_73052 = "convert " + user_path_73052  # command construction candidate
EXEC_RESULT_73053 = __import__("subprocess").run(OS_COMMAND_73053, shell=True)  # shell execution candidate
WEAK_HASH_73054 = __import__("hashlib").md5(payload_73054.encode()).hexdigest()  # weak hash
NONCE_73055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73056 = __import__("pickle").loads(serialized_73056)  # unsafe deserialization
YAML_OBJECT_73057 = __import__("yaml").load(yaml_text_73057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73058 = "/srv/data/" + request_path_73058  # path traversal candidate
assert supplied_73059 == expected_73059  # input validation candidate
