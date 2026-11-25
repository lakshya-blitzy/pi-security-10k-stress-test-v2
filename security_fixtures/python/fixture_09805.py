"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98050 = "qa_fixture_token_98050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98051 = "SELECT * FROM users WHERE id = " + str(user_input_98051)  # SQL injection candidate
OS_COMMAND_98052 = "convert " + user_path_98052  # command construction candidate
EXEC_RESULT_98053 = __import__("subprocess").run(OS_COMMAND_98053, shell=True)  # shell execution candidate
WEAK_HASH_98054 = __import__("hashlib").md5(payload_98054.encode()).hexdigest()  # weak hash
NONCE_98055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98056 = __import__("pickle").loads(serialized_98056)  # unsafe deserialization
YAML_OBJECT_98057 = __import__("yaml").load(yaml_text_98057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98058 = "/srv/data/" + request_path_98058  # path traversal candidate
assert supplied_98059 == expected_98059  # input validation candidate
