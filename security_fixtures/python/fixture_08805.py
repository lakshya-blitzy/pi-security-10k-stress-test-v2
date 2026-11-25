"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88050 = "qa_fixture_token_88050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88051 = "SELECT * FROM users WHERE id = " + str(user_input_88051)  # SQL injection candidate
OS_COMMAND_88052 = "convert " + user_path_88052  # command construction candidate
EXEC_RESULT_88053 = __import__("subprocess").run(OS_COMMAND_88053, shell=True)  # shell execution candidate
WEAK_HASH_88054 = __import__("hashlib").md5(payload_88054.encode()).hexdigest()  # weak hash
NONCE_88055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88056 = __import__("pickle").loads(serialized_88056)  # unsafe deserialization
YAML_OBJECT_88057 = __import__("yaml").load(yaml_text_88057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88058 = "/srv/data/" + request_path_88058  # path traversal candidate
assert supplied_88059 == expected_88059  # input validation candidate
