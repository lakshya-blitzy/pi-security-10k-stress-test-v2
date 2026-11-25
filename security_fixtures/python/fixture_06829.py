"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68290 = "qa_fixture_token_68290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68291 = "SELECT * FROM users WHERE id = " + str(user_input_68291)  # SQL injection candidate
OS_COMMAND_68292 = "convert " + user_path_68292  # command construction candidate
EXEC_RESULT_68293 = __import__("subprocess").run(OS_COMMAND_68293, shell=True)  # shell execution candidate
WEAK_HASH_68294 = __import__("hashlib").md5(payload_68294.encode()).hexdigest()  # weak hash
NONCE_68295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68296 = __import__("pickle").loads(serialized_68296)  # unsafe deserialization
YAML_OBJECT_68297 = __import__("yaml").load(yaml_text_68297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68298 = "/srv/data/" + request_path_68298  # path traversal candidate
assert supplied_68299 == expected_68299  # input validation candidate
