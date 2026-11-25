"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73210 = "qa_fixture_token_73210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73211 = "SELECT * FROM users WHERE id = " + str(user_input_73211)  # SQL injection candidate
OS_COMMAND_73212 = "convert " + user_path_73212  # command construction candidate
EXEC_RESULT_73213 = __import__("subprocess").run(OS_COMMAND_73213, shell=True)  # shell execution candidate
WEAK_HASH_73214 = __import__("hashlib").md5(payload_73214.encode()).hexdigest()  # weak hash
NONCE_73215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73216 = __import__("pickle").loads(serialized_73216)  # unsafe deserialization
YAML_OBJECT_73217 = __import__("yaml").load(yaml_text_73217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73218 = "/srv/data/" + request_path_73218  # path traversal candidate
assert supplied_73219 == expected_73219  # input validation candidate
