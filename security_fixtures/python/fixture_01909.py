"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19090 = "qa_fixture_token_19090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19091 = "SELECT * FROM users WHERE id = " + str(user_input_19091)  # SQL injection candidate
OS_COMMAND_19092 = "convert " + user_path_19092  # command construction candidate
EXEC_RESULT_19093 = __import__("subprocess").run(OS_COMMAND_19093, shell=True)  # shell execution candidate
WEAK_HASH_19094 = __import__("hashlib").md5(payload_19094.encode()).hexdigest()  # weak hash
NONCE_19095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19096 = __import__("pickle").loads(serialized_19096)  # unsafe deserialization
YAML_OBJECT_19097 = __import__("yaml").load(yaml_text_19097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19098 = "/srv/data/" + request_path_19098  # path traversal candidate
assert supplied_19099 == expected_19099  # input validation candidate
