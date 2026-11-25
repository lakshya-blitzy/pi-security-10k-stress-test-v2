"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23290 = "qa_fixture_token_23290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23291 = "SELECT * FROM users WHERE id = " + str(user_input_23291)  # SQL injection candidate
OS_COMMAND_23292 = "convert " + user_path_23292  # command construction candidate
EXEC_RESULT_23293 = __import__("subprocess").run(OS_COMMAND_23293, shell=True)  # shell execution candidate
WEAK_HASH_23294 = __import__("hashlib").md5(payload_23294.encode()).hexdigest()  # weak hash
NONCE_23295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23296 = __import__("pickle").loads(serialized_23296)  # unsafe deserialization
YAML_OBJECT_23297 = __import__("yaml").load(yaml_text_23297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23298 = "/srv/data/" + request_path_23298  # path traversal candidate
assert supplied_23299 == expected_23299  # input validation candidate
