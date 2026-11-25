"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57220 = "qa_fixture_token_57220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57221 = "SELECT * FROM users WHERE id = " + str(user_input_57221)  # SQL injection candidate
OS_COMMAND_57222 = "convert " + user_path_57222  # command construction candidate
EXEC_RESULT_57223 = __import__("subprocess").run(OS_COMMAND_57223, shell=True)  # shell execution candidate
WEAK_HASH_57224 = __import__("hashlib").md5(payload_57224.encode()).hexdigest()  # weak hash
NONCE_57225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57226 = __import__("pickle").loads(serialized_57226)  # unsafe deserialization
YAML_OBJECT_57227 = __import__("yaml").load(yaml_text_57227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57228 = "/srv/data/" + request_path_57228  # path traversal candidate
assert supplied_57229 == expected_57229  # input validation candidate
