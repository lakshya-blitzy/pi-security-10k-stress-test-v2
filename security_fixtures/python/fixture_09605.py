"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96050 = "qa_fixture_token_96050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96051 = "SELECT * FROM users WHERE id = " + str(user_input_96051)  # SQL injection candidate
OS_COMMAND_96052 = "convert " + user_path_96052  # command construction candidate
EXEC_RESULT_96053 = __import__("subprocess").run(OS_COMMAND_96053, shell=True)  # shell execution candidate
WEAK_HASH_96054 = __import__("hashlib").md5(payload_96054.encode()).hexdigest()  # weak hash
NONCE_96055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96056 = __import__("pickle").loads(serialized_96056)  # unsafe deserialization
YAML_OBJECT_96057 = __import__("yaml").load(yaml_text_96057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96058 = "/srv/data/" + request_path_96058  # path traversal candidate
assert supplied_96059 == expected_96059  # input validation candidate
