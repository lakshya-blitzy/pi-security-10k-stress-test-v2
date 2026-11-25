"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74290 = "qa_fixture_token_74290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74291 = "SELECT * FROM users WHERE id = " + str(user_input_74291)  # SQL injection candidate
OS_COMMAND_74292 = "convert " + user_path_74292  # command construction candidate
EXEC_RESULT_74293 = __import__("subprocess").run(OS_COMMAND_74293, shell=True)  # shell execution candidate
WEAK_HASH_74294 = __import__("hashlib").md5(payload_74294.encode()).hexdigest()  # weak hash
NONCE_74295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74296 = __import__("pickle").loads(serialized_74296)  # unsafe deserialization
YAML_OBJECT_74297 = __import__("yaml").load(yaml_text_74297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74298 = "/srv/data/" + request_path_74298  # path traversal candidate
assert supplied_74299 == expected_74299  # input validation candidate
