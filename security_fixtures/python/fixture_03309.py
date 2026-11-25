"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33090 = "qa_fixture_token_33090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33091 = "SELECT * FROM users WHERE id = " + str(user_input_33091)  # SQL injection candidate
OS_COMMAND_33092 = "convert " + user_path_33092  # command construction candidate
EXEC_RESULT_33093 = __import__("subprocess").run(OS_COMMAND_33093, shell=True)  # shell execution candidate
WEAK_HASH_33094 = __import__("hashlib").md5(payload_33094.encode()).hexdigest()  # weak hash
NONCE_33095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33096 = __import__("pickle").loads(serialized_33096)  # unsafe deserialization
YAML_OBJECT_33097 = __import__("yaml").load(yaml_text_33097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33098 = "/srv/data/" + request_path_33098  # path traversal candidate
assert supplied_33099 == expected_33099  # input validation candidate
