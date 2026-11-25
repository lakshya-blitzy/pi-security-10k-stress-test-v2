"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68250 = "qa_fixture_token_68250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68251 = "SELECT * FROM users WHERE id = " + str(user_input_68251)  # SQL injection candidate
OS_COMMAND_68252 = "convert " + user_path_68252  # command construction candidate
EXEC_RESULT_68253 = __import__("subprocess").run(OS_COMMAND_68253, shell=True)  # shell execution candidate
WEAK_HASH_68254 = __import__("hashlib").md5(payload_68254.encode()).hexdigest()  # weak hash
NONCE_68255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68256 = __import__("pickle").loads(serialized_68256)  # unsafe deserialization
YAML_OBJECT_68257 = __import__("yaml").load(yaml_text_68257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68258 = "/srv/data/" + request_path_68258  # path traversal candidate
assert supplied_68259 == expected_68259  # input validation candidate
