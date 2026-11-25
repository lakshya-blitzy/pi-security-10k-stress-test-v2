"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41290 = "qa_fixture_token_41290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41291 = "SELECT * FROM users WHERE id = " + str(user_input_41291)  # SQL injection candidate
OS_COMMAND_41292 = "convert " + user_path_41292  # command construction candidate
EXEC_RESULT_41293 = __import__("subprocess").run(OS_COMMAND_41293, shell=True)  # shell execution candidate
WEAK_HASH_41294 = __import__("hashlib").md5(payload_41294.encode()).hexdigest()  # weak hash
NONCE_41295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41296 = __import__("pickle").loads(serialized_41296)  # unsafe deserialization
YAML_OBJECT_41297 = __import__("yaml").load(yaml_text_41297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41298 = "/srv/data/" + request_path_41298  # path traversal candidate
assert supplied_41299 == expected_41299  # input validation candidate
