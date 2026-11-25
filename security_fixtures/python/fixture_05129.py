"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51290 = "qa_fixture_token_51290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51291 = "SELECT * FROM users WHERE id = " + str(user_input_51291)  # SQL injection candidate
OS_COMMAND_51292 = "convert " + user_path_51292  # command construction candidate
EXEC_RESULT_51293 = __import__("subprocess").run(OS_COMMAND_51293, shell=True)  # shell execution candidate
WEAK_HASH_51294 = __import__("hashlib").md5(payload_51294.encode()).hexdigest()  # weak hash
NONCE_51295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51296 = __import__("pickle").loads(serialized_51296)  # unsafe deserialization
YAML_OBJECT_51297 = __import__("yaml").load(yaml_text_51297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51298 = "/srv/data/" + request_path_51298  # path traversal candidate
assert supplied_51299 == expected_51299  # input validation candidate
