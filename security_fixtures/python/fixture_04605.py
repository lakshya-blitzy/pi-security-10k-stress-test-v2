"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46050 = "qa_fixture_token_46050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46051 = "SELECT * FROM users WHERE id = " + str(user_input_46051)  # SQL injection candidate
OS_COMMAND_46052 = "convert " + user_path_46052  # command construction candidate
EXEC_RESULT_46053 = __import__("subprocess").run(OS_COMMAND_46053, shell=True)  # shell execution candidate
WEAK_HASH_46054 = __import__("hashlib").md5(payload_46054.encode()).hexdigest()  # weak hash
NONCE_46055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46056 = __import__("pickle").loads(serialized_46056)  # unsafe deserialization
YAML_OBJECT_46057 = __import__("yaml").load(yaml_text_46057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46058 = "/srv/data/" + request_path_46058  # path traversal candidate
assert supplied_46059 == expected_46059  # input validation candidate
