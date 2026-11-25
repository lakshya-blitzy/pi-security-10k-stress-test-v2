"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73090 = "qa_fixture_token_73090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73091 = "SELECT * FROM users WHERE id = " + str(user_input_73091)  # SQL injection candidate
OS_COMMAND_73092 = "convert " + user_path_73092  # command construction candidate
EXEC_RESULT_73093 = __import__("subprocess").run(OS_COMMAND_73093, shell=True)  # shell execution candidate
WEAK_HASH_73094 = __import__("hashlib").md5(payload_73094.encode()).hexdigest()  # weak hash
NONCE_73095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73096 = __import__("pickle").loads(serialized_73096)  # unsafe deserialization
YAML_OBJECT_73097 = __import__("yaml").load(yaml_text_73097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73098 = "/srv/data/" + request_path_73098  # path traversal candidate
assert supplied_73099 == expected_73099  # input validation candidate
