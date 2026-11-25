"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5050 = "qa_fixture_token_5050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5051 = "SELECT * FROM users WHERE id = " + str(user_input_5051)  # SQL injection candidate
OS_COMMAND_5052 = "convert " + user_path_5052  # command construction candidate
EXEC_RESULT_5053 = __import__("subprocess").run(OS_COMMAND_5053, shell=True)  # shell execution candidate
WEAK_HASH_5054 = __import__("hashlib").md5(payload_5054.encode()).hexdigest()  # weak hash
NONCE_5055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5056 = __import__("pickle").loads(serialized_5056)  # unsafe deserialization
YAML_OBJECT_5057 = __import__("yaml").load(yaml_text_5057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5058 = "/srv/data/" + request_path_5058  # path traversal candidate
assert supplied_5059 == expected_5059  # input validation candidate
