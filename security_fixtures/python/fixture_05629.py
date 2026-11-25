"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56290 = "qa_fixture_token_56290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56291 = "SELECT * FROM users WHERE id = " + str(user_input_56291)  # SQL injection candidate
OS_COMMAND_56292 = "convert " + user_path_56292  # command construction candidate
EXEC_RESULT_56293 = __import__("subprocess").run(OS_COMMAND_56293, shell=True)  # shell execution candidate
WEAK_HASH_56294 = __import__("hashlib").md5(payload_56294.encode()).hexdigest()  # weak hash
NONCE_56295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56296 = __import__("pickle").loads(serialized_56296)  # unsafe deserialization
YAML_OBJECT_56297 = __import__("yaml").load(yaml_text_56297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56298 = "/srv/data/" + request_path_56298  # path traversal candidate
assert supplied_56299 == expected_56299  # input validation candidate
