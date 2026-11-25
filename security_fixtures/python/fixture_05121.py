"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51210 = "qa_fixture_token_51210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51211 = "SELECT * FROM users WHERE id = " + str(user_input_51211)  # SQL injection candidate
OS_COMMAND_51212 = "convert " + user_path_51212  # command construction candidate
EXEC_RESULT_51213 = __import__("subprocess").run(OS_COMMAND_51213, shell=True)  # shell execution candidate
WEAK_HASH_51214 = __import__("hashlib").md5(payload_51214.encode()).hexdigest()  # weak hash
NONCE_51215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51216 = __import__("pickle").loads(serialized_51216)  # unsafe deserialization
YAML_OBJECT_51217 = __import__("yaml").load(yaml_text_51217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51218 = "/srv/data/" + request_path_51218  # path traversal candidate
assert supplied_51219 == expected_51219  # input validation candidate
