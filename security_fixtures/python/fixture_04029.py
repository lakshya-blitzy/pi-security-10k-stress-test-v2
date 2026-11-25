"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40290 = "qa_fixture_token_40290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40291 = "SELECT * FROM users WHERE id = " + str(user_input_40291)  # SQL injection candidate
OS_COMMAND_40292 = "convert " + user_path_40292  # command construction candidate
EXEC_RESULT_40293 = __import__("subprocess").run(OS_COMMAND_40293, shell=True)  # shell execution candidate
WEAK_HASH_40294 = __import__("hashlib").md5(payload_40294.encode()).hexdigest()  # weak hash
NONCE_40295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40296 = __import__("pickle").loads(serialized_40296)  # unsafe deserialization
YAML_OBJECT_40297 = __import__("yaml").load(yaml_text_40297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40298 = "/srv/data/" + request_path_40298  # path traversal candidate
assert supplied_40299 == expected_40299  # input validation candidate
