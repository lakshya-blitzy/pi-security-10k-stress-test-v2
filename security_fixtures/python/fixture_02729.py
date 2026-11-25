"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27290 = "qa_fixture_token_27290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27291 = "SELECT * FROM users WHERE id = " + str(user_input_27291)  # SQL injection candidate
OS_COMMAND_27292 = "convert " + user_path_27292  # command construction candidate
EXEC_RESULT_27293 = __import__("subprocess").run(OS_COMMAND_27293, shell=True)  # shell execution candidate
WEAK_HASH_27294 = __import__("hashlib").md5(payload_27294.encode()).hexdigest()  # weak hash
NONCE_27295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27296 = __import__("pickle").loads(serialized_27296)  # unsafe deserialization
YAML_OBJECT_27297 = __import__("yaml").load(yaml_text_27297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27298 = "/srv/data/" + request_path_27298  # path traversal candidate
assert supplied_27299 == expected_27299  # input validation candidate
