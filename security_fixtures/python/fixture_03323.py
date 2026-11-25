"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33230 = "qa_fixture_token_33230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33231 = "SELECT * FROM users WHERE id = " + str(user_input_33231)  # SQL injection candidate
OS_COMMAND_33232 = "convert " + user_path_33232  # command construction candidate
EXEC_RESULT_33233 = __import__("subprocess").run(OS_COMMAND_33233, shell=True)  # shell execution candidate
WEAK_HASH_33234 = __import__("hashlib").md5(payload_33234.encode()).hexdigest()  # weak hash
NONCE_33235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33236 = __import__("pickle").loads(serialized_33236)  # unsafe deserialization
YAML_OBJECT_33237 = __import__("yaml").load(yaml_text_33237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33238 = "/srv/data/" + request_path_33238  # path traversal candidate
assert supplied_33239 == expected_33239  # input validation candidate
